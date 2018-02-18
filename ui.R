library(shiny)


shinyUI(dashboardPage(skin = "blue",
  dashboardHeader(title = "Cost of Living Generator",titleWidth = 250),
  
  sidebar <-  
    dashboardSidebar(width = 250,
      sidebarMenu(id='sideBarMenu',
                  menuItem("Income Input", tabName = "About", icon = icon("address-card")),
                  menuItem("Monthly Costs", tabName = "EDA", icon = icon("dashboard"),badgeLabel = "Data", badgeColor = "green")
                  ),
      conditionalPanel("input.sideBarMenu == 'About'",
                       selectizeInput(inputId = "Adults",
                                      label = "Single or Married:",
                                      choices = c("Single","Married")),
                       selectizeInput(inputId = "kids",
                                      label = "Number of Kids:",
                                      choices = c("0","1","2","3","4"),
                                      selected = "0"),
                       
                       selectizeInput(inputId = "Locational",
                                      label = "Locational Preference:",
                                      choices = c("City Center","Outside City Center"),
                                      selected = "City Center"),
                       
                       selectizeInput(inputId = "Transportation",
                                      label = "Transportation Method:",
                                      choices = c("Personal Car","Public Transportation"),
                                      selected = "Personal Car"),
                       
                       sliderInput("Meals", "Meals Purchased Per Week:",
                                   min = 0, max = 30,
                                   value = 0)
    ),
      conditionalPanel("input.sideBarMenu == 'EDA'",
                      selectizeInput(inputId = "Adults1",
                                     label = "Single or Married:",
                                     choices = c("Single","Married")),
                      selectizeInput(inputId = "kids1",
                                     label = "Number of Kids:",
                                     choices = c("0","1","2","3","4"),
                                     selected = "0"),
                      
                      selectizeInput(inputId = "Locational1",
                                     label = "Locational Preference:",
                                     choices = c("City Center","Outside City Center"),
                                     selected = "City Center"),
                      
                      selectizeInput(inputId = "Transportation1",
                                     label = "Transportation Method:",
                                     choices = c("Personal Car","Public Transportation"),
                                     selected = "Personal Car"),
                      
                      sliderInput("Meals1", "Meals Purchased Per Week:",
                                  min = 0, max = 30,
                                  value = 0)
    )),
    body <- dashboardBody(
      tabItems(
        tabItem(
          
          tabName = "About",
          fluidRow(align = "center",box(width = 12,
                                        h2(tags$b(tags$em("Welcome to Cost of Living Generator"))),
                                        tags$hr(),
                                        h4(tags$u('Explore cost of living parameters across  
                                           markets in the U.S.')),
                                        img(src = "fitness.png",height = 60L),
                                        img(src = "childcare.png",height = 60L),
                                        img(src = "clothes.png",height = 60L),
                                        img(src = "home.png",height = 80L),
                                        img(src = "gas.png",height = 60L)
                                        )),
          fluidRow(align="center",
                   box(textInput("income", label = h4(tags$b(tags$u("Enter Household Monthly Take-Home Income ($):"))), value = "3000"),
                   selectizeInput('region',label = 'Region:',choices = unique(goods[, Region]),multiple = FALSE,selected = "East")),
          
                  infoBoxOutput(outputId = "avg_col"),
                  infoBoxOutput(outputId = "dis_avg")),
          fluidRow(box(plotOutput(outputId = "monthlycost"),width=6),
                  box(plotOutput(outputId = "disposable"),width=6)
                  )
        ),

                
      

          
          
        tabItem(   
          tabName = "EDA",
          #titlePanel(tags$b("Cost of Living Benchmark")),
          fluidRow(box(
          selectizeInput('citytype1',label = 'City Profile:',choices = unique(goods[, Classification]),multiple = FALSE,selected = "24-Hour City")),
          infoBoxOutput(outputId = "avgBox1")
          ),
          br(),
          leafletOutput("mymap"),
          fluidRow(box(DT::dataTableOutput("table"), width = 12)))
          #fluidRow(box(plotOutput(outputId = "regioncol")))
      )
    )
  
  
))
