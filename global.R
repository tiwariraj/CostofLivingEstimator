###NYCDSA Bootcamp 12, Web Scrapping Project###
###Raj Tiwari###

library(shiny)
library(data.table)
library(dplyr)
library(leaflet)
library(leaflet.extras)
library(ggplot2)
library(shinythemes)
library(tidyr)
library(DT)
library(googleVis)
library(maps)
library(shinydashboard)
library(plotly)
library(ggrepel)

goods <- fread(file = "goods.csv")
