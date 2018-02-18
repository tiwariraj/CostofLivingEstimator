library(shiny)
library(dplyr)
library(tidyr)
library(ggplot2)
library(ggrepel)

function(input, output, session) {
  
  incomecalc_region <- reactive({
    goods = goods %>% 
      filter(Region == input$region)

    #Build Monthly Cost Estimate
    goods$MonthlyCost = goods$BasicUtilities + goods$Internet +
      goods$ClothesMonthlyAvg*(if_else(input$Adults=="Single",1,2)) +
      goods$ClothesMonthlyAvg*(as.numeric(input$kids)*.5)  +
      goods$Childcare*(as.numeric(input$kids)) + 
      goods$MonthlyPass*(if_else(input$Transportation=="Public Transportation",(if_else(input$Adults=="Single",1,2)),0)) + 
      goods$GasPrice*(50)*(if_else(input$Transportation=="Personal Car",(if_else(input$Adults=="Single",1,2)),0)) + 
      ((goods$Food*(if_else(input$Adults=="Single",1,2)))/90)*(90-input$Meals) +
      goods$Food*(if_else(input$kids=="0",0,if_else(input$kids=="1",1,2))) +
      (as.numeric(goods$InexpensiveMeal) * input$Meals*2) + 
      (goods$Rent3Br_OutsideCenter*(if_else(input$Adults=="Single",0,1))*(if_else(input$Locational=="City Center",0,1))) +
      (goods$Rent1Br_OutsideCenter*(if_else(input$Adults=="Single",1,0))*(if_else(input$Locational=="City Center",0,1))) +
      (goods$Rent3Br_CityCenter*(if_else(input$Adults=="Single",0,1))*(if_else(input$Locational=="City Center",1,0))) +
      (goods$Rent1Br_CityCenter*(if_else(input$Adults=="Single",1,0))*(if_else(input$Locational=="City Center",1,0)))
    
    goods$OverallMonthlyCost = mean(goods$MonthlyCost,na.rm = TRUE)
    #goods$income = goods$MonthlySalary*(ifelse(input$Adults=="Single",1,2))
    
    goods$MarketIndex = (goods$MonthlyCost/goods$OverallMonthlyCost)*100
    goods$HouseholdIncome = as.numeric(input$income)
    goods$DisposableIncome = goods$HouseholdIncome - goods$MonthlyCost
    return(goods)
  })
  
  monthlycost <- reactive({
    goods=goods %>% 
      filter(Classification == input$citytype1)

    goods$MonthlyCost = goods$BasicUtilities + goods$Internet +
      goods$ClothesMonthlyAvg*(if_else(input$Adults1=="Single",1,2)) +
      goods$ClothesMonthlyAvg*(as.numeric(input$kids1)*.5)  +
      goods$Childcare*(as.numeric(input$kids1)) + 
      goods$MonthlyPass*(if_else(input$Transportation1=="Public Transportation",(if_else(input$Adults1=="Single",1,2)),0)) + 
      goods$GasPrice*(50)*(if_else(input$Transportation1=="Personal Car",(if_else(input$Adults1=="Single",1,2)),0)) + 
      ((goods$Food*(if_else(input$Adults1=="Single",1,2)))/90)*(90-input$Meals1) +
      goods$Food*(if_else(input$kids1=="0",0,if_else(input$kids1=="1",1,2))) +
      (as.numeric(goods$InexpensiveMeal) * input$Meals1*2) + 
      (goods$Rent3Br_OutsideCenter*(if_else(input$Adults1=="Single",0,1))*(if_else(input$Locational1=="City Center",0,1))) +
      (goods$Rent1Br_OutsideCenter*(if_else(input$Adults1=="Single",1,0))*(if_else(input$Locational1=="City Center",0,1))) +
      (goods$Rent3Br_CityCenter*(if_else(input$Adults1=="Single",0,1))*(if_else(input$Locational1=="City Center",1,0))) +
      (goods$Rent1Br_CityCenter*(if_else(input$Adults1=="Single",1,0))*(if_else(input$Locational1=="City Center",1,0)))
    
    
    goods$OverallMonthlyCost = mean(goods$MonthlyCost,na.rm = TRUE)
    #goods$income = goods$MonthlySalary*(ifelse(input$Adults=="Single",1,2))
    
    goods$MarketIndex = (goods$MonthlyCost/goods$OverallMonthlyCost)*100
    goods$MarketIndex = round(goods$MarketIndex,2)
    goods$MonthlyCost = round(goods$MonthlyCost,2)

    return(goods)
  })
  
  ###Show statistics using infoBox###
  # output$regioncol <- renderPlot({
  #   x = monthlycost() %>% 
  #     group_by(Region) %>% 
  #     summarise(Monthly_CostofLiving = mean(MonthlyCost,na.rm=TRUE))
  #   
  #   
  #   p <- ggplot(x, aes(x=Region,y=Monthly_CostofLiving)) + geom_bar(position="dodge", stat="identity") +
  #     labs(y="Monthly Cost of Living ($)",title="Average Monthly Cost ($) by Region")
  #   p 
  #   
  # })
  
  output$regioncol <- renderPlot({
    x = monthlycost() %>% 
      group_by(Region) %>% 
      summarise(Monthly_CostofLiving = mean(MonthlyCost))
    
    
    p <- ggplot(x, aes(x=Region,y=Monthly_CostofLiving)) + geom_bar(position="dodge", stat="identity") +
      labs(y="Monthly Cost of Living ($)",title="Average Monthly Cost ($) by Region")
    p 
    
  })
  
  output$avgBox1 <- renderInfoBox({
    x = monthlycost()
    
    infoBox("Avg. Monthly Cost ($):",value = round(x$OverallMonthlyCost,2),icon = icon("calculator"), fill = TRUE)
  })
  
  output$disposable <- renderPlot({
    x = incomecalc_region()
    p <- ggplot(data = x,aes(x =MonthlyCost, y= DisposableIncome,label=MarketName,color=Classification)) + 
       geom_point() +geom_text_repel(aes(label=MarketName)) +
       labs(title = "Avg. Monthly Cost of Living ($) by Disposable Income") 
    p 
  })
  
  

  output$monthlycost <- renderPlot({
    x = incomecalc_region()
    p <- ggplot(x, aes(x = reorder(MarketName, -MonthlyCost), y = MonthlyCost, fill = Classification)) +
      geom_bar(stat = "identity") + geom_hline(yintercept = x$OverallMonthlyCost)  + 
      labs(x="Market Name",title = "Avg. Monthly Cost of Living ($) by Market") + theme(legend.title = element_blank())
    p + theme(axis.text.x = element_text(angle = 90, hjust = 1)) +  theme(axis.title.y = element_text(margin = margin(t = 0, r = 20, b = 0, l = 0)))
    
  })
  
   output$dis_avg <- renderInfoBox({
     x = incomecalc_region() 
     infoBox("Avg. Disposable Income ($):",value = round(mean(x$DisposableIncome),2),icon = icon("calculator"), fill = TRUE)
   })
  
  output$avg_col <- renderInfoBox({
    x = incomecalc_region()

    infoBox("Avg. Monthly Cost ($):",value = round(x$OverallMonthlyCost,2),icon = icon("calculator"), fill = TRUE)
  })
   #######################################################################################################
   # show map using leafleet Render
  output$table <- DT::renderDataTable({
       x = monthlycost() %>% select(MarketName,MonthlyCost,MarketIndex,Internet,GasPrice,RunningShoes,FitnessClub)
       DT::datatable(x, options = list(pageLength = 15,background="skyblue", fontWeight='bold'))
     })
  
  
  
  output$mymap <- renderLeaflet({
    
    mydata <- monthlycost()  %>%
      mutate(group = cut(MonthlyCost, breaks = c(0, 4000, 7000, 10000, Inf),
                         labels = c("green", "orange", "red", "darkred"),
                         include.lowest = TRUE)) %>%
      rename(x = Long, y = Lat)
    
    icons <- awesomeIcons(markerColor = mydata$group)
    
    leaflet(mydata) %>%
      addProviderTiles("Esri.WorldStreetMap") %>%
      addAwesomeMarkers(~x, ~y,label = as.character(mydata$MarketName),icon=icons,
                        #label==~as.character(cost$MarketName),
                        popup=paste("Avg. Monthly Cost ($):", 
                                    round(mydata$MonthlyCost,2),"<br>"
                                    ,"Index:", round(mydata$MarketIndex,2),"<br>"
                               ))

  })
}