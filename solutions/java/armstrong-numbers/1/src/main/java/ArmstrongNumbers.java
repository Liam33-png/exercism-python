class ArmstrongNumbers {

    boolean isArmstrongNumber(int numberToCheck) {
        int total = 0;
        for(int i = 0; i < String.valueOf(numberToCheck).length(); i++){
            total += Math.pow(Character.getNumericValue(String.valueOf(numberToCheck).charAt(i)), String.valueOf(numberToCheck).length());
        }
        return total == numberToCheck;
        }

}
