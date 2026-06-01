class NeedForSpeed {
    public int speed;
    public int batteryDrain;
    public int battery = 100;
    public int miles;
    NeedForSpeed(int speed, int batteryDrain) {
        this.speed = speed;
        this.batteryDrain = batteryDrain;
    }

    public boolean batteryDrained() {
        return this.battery - this.batteryDrain < 0;
    }

    public int distanceDriven() {
        return this.miles;
    }

    public void drive() {
        if (this.battery > 0){
            this.battery -= this.batteryDrain;
            this.miles += this.speed;
        }
    }

    public static NeedForSpeed nitro() {
        return new NeedForSpeed(50, 4);
    }
}

class RaceTrack {
    int distance;
    RaceTrack(int distance) {
        this.distance = distance;
    }

    public boolean canFinishRace(NeedForSpeed car) {
        return car.battery / car.batteryDrain * car.speed >= this.distance;
    }
}
