# Filename: torque-wrench.R
# Date: April 6, 2010
# Author: Jason Moore
# Description: Analyzes the data from the bicycle torque wrench experiments
# performed on April 6, 2010.

rm(list = ls())

# read the data
data <- read.csv('torque-wrench-data.txt')

# miles per hour to meters per second
mph2mps = 0.44704
# inch pounds to newton meters
inchlb2nm = 0.112984829

averageSpeed <- (data$MaxSpeed + data$MinSpeed) / 2

"../../figures/davisbicycle/" -> figDir

# histogram of the average run speeds
png(paste(figDir, "twrench-speed-histogram.png", sep=""),
	width=800, height=800, pointsize=10, res=200)
hist(averageSpeed)
dev.off()

# histogram of the max/min torque values
png(paste(figDir, "twrench-torque-histogram.png", sep=""),
	width=800, height=800, pointsize=10, res=200)
hist(abs(c(data$MinTorque, inchlb2nm * data$MaxTorque)), main ="Histogram
of Torque Values", xlab="Absolute value of max and min torques [Nm]", breaks=25)
dev.off()

# torque versus speed for all the runs
png(paste(figDir, "twrench-torque-speed.png", sep=""),
	width=800, height=800, pointsize=10, res=200)
plot(0:10,-5:5, type="n", main="Max and Min Torques as a Function of Speed",
xlab="Speed [m/s]", ylab="Torque [Nm]")
points(mph2mps * averageSpeed, data$MinTorque, pch=19)
points(mph2mps * averageSpeed, inchlb2nm * data$MaxTorque, pch=23)
dev.off()

maneuvers <- unique(data$Maneuver)
print(maneuvers)
for(maneuver in levels(maneuvers)){
    print(maneuver)
    png(paste(figDir, "twrench-", maneuver, ".png", sep=""))
    x <- subset(mph2mps*averageSpeed, data$Maneuver==maneuver)
    y <- subset(data$MinTorque, data$Maneuver==maneuver)
    y2 <- subset(inchlb2nm*data$MaxTorque, data$Maneuver==maneuver)
    plot(0:10,-5:5, type="n", main=maneuver, xlab="Speed [m/s]", ylab="Torque [Nm]")
    points(x, y)
    points(x, y2)
    arrows(x, y, x, y2, length=0)
    dev.off()
    maxTorque <- max(y2, na.rm=TRUE)
    minTorque <- min(y, na.rm=TRUE)
    print(paste("Max and min torque for ", maneuver, " = ", maxTorque, " and ",
    minTorque))
    }
