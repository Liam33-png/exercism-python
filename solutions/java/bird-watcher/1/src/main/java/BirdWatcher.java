
class BirdWatcher {
    private final int[] birdsPerDay;

    public BirdWatcher(int[] birdsPerDay) {
        this.birdsPerDay = birdsPerDay.clone();
    }

    public static int[] getLastWeek() {
        int[] lastWeek = new int[]{0, 2, 5, 3, 7, 8, 4};
        return lastWeek;
    }

    public int getToday() {
        return this.birdsPerDay[this.birdsPerDay.length - 1];
    }

    public void incrementTodaysCount() {
        this.birdsPerDay[this.birdsPerDay.length - 1] = this.birdsPerDay[this.birdsPerDay.length - 1] + 1;
    }

    public boolean hasDayWithoutBirds() {
        for (int count: this.birdsPerDay){
            if (count == 0){
                return true;
            }
            }
        return false;
        }

    public int getCountForFirstDays(int numberOfDays) {
        int count = 0;
        for(int i = 0; i < numberOfDays; i++){
            if (i < this.birdsPerDay.length){
                count += this.birdsPerDay[i];
            }
        }
        return count;
    }

    public int getBusyDays() {
        int count = 0;
        for (int spotted : this.birdsPerDay ){
            if (spotted >= 5){
                count += 1;
            }
        }
        return count;
    }
}
