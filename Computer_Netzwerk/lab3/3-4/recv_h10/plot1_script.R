# Daten aus der TSV-Datei lesen
 data <- read.table("recv_h10.tsv")
 
 time <- data$V1
 bandwidth <- data$V2
 
  # PDF-Grafik erzeugen
 pdf("recv_h10_plot.pdf")
 
  # Liniendiagramm erstellen
 plot(time, bandwidth, type = "l", xlab = "Zeit in sec", ylab = "Datenrate in MB/sec", main = "iperf Ergebnisse", col= "red")
 
 # PDF-Grafik beenden
 dev.off()

