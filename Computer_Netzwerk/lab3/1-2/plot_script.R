# Daten aus der TSV-Datei lesen
 data <- read.table("h1.tsv")
 
 time <- data$V1
 bandwidth <- data$V2
 
 # PDF-Grafik erzeugen
 pdf("h1_plot.pdf")
 
 # Liniendiagramm erstellen
 plot(time, bandwidth, type = "l", xlab = "Zeit", ylab = "Datenrate", main = "iperf Ergebnisse")

# PDF-Grafik beenden
 dev.off()

