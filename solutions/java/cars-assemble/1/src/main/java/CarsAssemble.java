public class CarsAssemble {

    public double productionRatePerHour(int speed) {
        double sucessRate = 1;
        if (speed == 0){
            return 0;
        }
        else if (speed >=5 && speed <= 8){
            sucessRate = 0.9;
        }
        else if (speed == 9){
            sucessRate = 0.8;
        }
        else if (speed == 10){
            sucessRate = 0.77;
        }
        return speed * 221 * sucessRate;
        
    }

    public int workingItemsPerMinute(int speed) {
        return (int)productionRatePerHour(speed) / 60;
    }
}
