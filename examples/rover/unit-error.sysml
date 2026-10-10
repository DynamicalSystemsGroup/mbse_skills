package Rover {
    private import ISQ::*;
    private import SI::*;
    private import ScalarValues::*;
    attribute distance : LengthValue = 2000 [m];
    attribute speed : SpeedValue = 1 [m/s];
    attribute power : PowerValue = 100 [W];
    attribute capacity : EnergyValue = 270000 [m];
    attribute reserve : Real = 0.2;
    attribute duration : DurationValue = distance / speed;
    attribute usedEnergy : EnergyValue = power * duration;
    attribute remaining : Real = (capacity - usedEnergy) / capacity;
    constraint energyReserve { remaining >= reserve }
}
