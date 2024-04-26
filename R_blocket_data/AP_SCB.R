#install.packages("pxweb")
library(pxweb)
library("readxl")
library(tidyr)
library(scales)
library(ggplot2)

#d2<- pxweb_interactive("https://api.scb.se/OV0104/v1/doris/sv/ssd/START/TK/TK1001/TK1001A/FordonTrafik")
#df2<- subset(d2$data)
#View(df2)

# Define the API endpoint for the dataset
#api_data <- pxweb_interactive("https://api.scb.se/OV0104/v1/doris/sv/ssd/START/TK/TK1001/TK1001A/PersBilarDrivMedel")
file_path <- "C:/Users/magda/Skolarbete/R/i_trafik_2.xlsx"
car_data <- read_excel(file_path)
file_path2 <- "C:/Users/magda/Skolarbete/R/blocket_car_data.xlsx"
car_data_blocket <- read_excel(file_path2)
d <- pxweb_interactive("https://api.scb.se/OV0104/v1/doris/sv/ssd/START/TK/TK1001/TK1001A/FordonTrafik")

file_path3 <- "C:/Users/magda/Skolarbete/R/i_trafik_alla.xlsx"
car_data_alla_i_trafik <- read_excel(file_path3)

# Examine the data
View(car_data)
View(car_data_blocket)
View(car_data_alla_i_trafik)

duplicates <- duplicated(car_data_blocket)
car_data_blocket[duplicates, ]
# Ta bort duplicerade rader och behåll endast unika rader
car_data_unique <- car_data_blocket[!duplicated(car_data_blocket), ]

# Kontrollera antalet rader före och efter borttagningen
cat("Antal rader före borttagning:", nrow(car_data_blocket), "\n")
cat("Antal rader efter borttagning:", nrow(car_data_unique), "\n")


df_sub <- subset(d$data)

View(df_sub)
help("subset")
df_sub <- subset(d$data, region == "Riket" & fordonsslag == "personbilar")


car_data_long <- pivot_longer(car_data, 
                              cols = -år, 
                              names_to = "Fabrikat", 
                              values_to = "Antal")
# Check the structure of the filtered data
View(df_sub)
# Convert the 'år' column to numeric if it's not already
df_sub$år <- as.numeric(as.character(df_sub$år))
car_data_long$år <- as.numeric(as.character(car_data_long$år))

# After conversion, you can proceed with plotting as described earlier



label_years <- c(2005, 2010, 2015, 2020)

# Create a new column in df_sub for labels that only includes values for specific years
df_sub$label <- ifelse(df_sub$år %in% label_years, as.character(df_sub$`Fordon i trafik`), NA)

# Define the maximum values for each y-axis to determine the scale for the secondary y-axis
max_primary <- max(df_sub$`Fordon i trafik`, na.rm = TRUE)
max_secondary <- max(car_data_long$Antal, na.rm = TRUE)

gg <- ggplot() +
  geom_bar(data = car_data_long, aes(x = år, y = Antal / max_secondary * max_primary, fill = Fabrikat), 
           position = "stack", stat = "identity") +
  scale_y_continuous(
    name = "Fordon i trafik",
    labels = scales::comma,
    sec.axis = sec_axis(~ . * max_secondary / max_primary, name = "Antal årsmodell per Fabrikat")
  ) +
  geom_line(data = df_sub, aes(x = år, y = `Fordon i trafik`, group = 1), 
            color = "black", size = 1) +
  geom_text(data = df_sub, aes(x = år, y = `Fordon i trafik`, label = label), 
            vjust = -0.5, size = 3, na.rm = TRUE) +
  labs(title = "Antal Fordon i Trafik och Per Fabrikat över Åren",
       x = "År", y = "Antal") +
  theme_minimal() +
  scale_fill_brewer(palette = "Paired")

print(gg)



gg2 <- ggplot() +
  geom_line(data = df_sub, aes(x = år, y = `Fordon i trafik`, group = 1), 
            color = "black", size = 1) +
  geom_text(data = df_sub, aes(x = år, y = `Fordon i trafik`, label = `Fordon i trafik`), 
            vjust = -0.5, size = 3, na.rm = TRUE) +
  labs(title = "Antal Fordon i Trafik",
       x = "År", y = "Antal") +
  theme_minimal() +
  scale_fill_brewer(palette = "Paired")

print(gg2)


