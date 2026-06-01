public class JedliksToyCar {
    public int distanceDriven;
    public int battery = 100;
    public static JedliksToyCar buy() {
        return new JedliksToyCar();
    }

    public String distanceDisplay() {
        return "Driven " + String.valueOf(this.distanceDriven)  + " meters";
    }

    public String batteryDisplay() {
        if (this.battery == 0){
            return "Battery empty";
        }
        return "Battery at " + String.valueOf(this.battery) + "%";
    }

    public void drive() {
        if (this.battery > 0){
        this.battery -= 1;
        this.distanceDriven += 20;
        }
    }
}
