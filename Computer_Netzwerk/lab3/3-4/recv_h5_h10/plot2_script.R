# Daten aus der TSV-Datei lesen
 data <- read.table("h5_h10.tsv", header = FALSE)

# Daten für h5 und h10 extrahieren
 h5_data <- data[seq(1, nrow(data), by = 2), ]
 h10_data <- data[seq(2, nrow(data), by = 2), ]

# PDF-Grafik erzeugen
 pdf("h5_h10_plot.pdf")

# Liniendiagramm für h5 erstellen
 plot(h5_data$V1, h5_data$V2, type = "l", xlab = "Zeit in sec", ylab = "Datenrate in MB/sec", col = "blue", main = "iperf Ergebnisse")

# Liniendiagramm für h10 hinzufügen
 lines(h10_data$V1, h10_data$V2, type = "l", col = "red")

# Legende hinzufügen
 legend("topleft", legend = c("h5", "h10"), col = c("blue", "red"), lty = 1)

# PDF-Grafik beenden
 dev.off()

