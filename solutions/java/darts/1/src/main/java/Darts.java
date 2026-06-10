class Darts {
    int score(double xOfDart, double yOfDart) {
        if (Math.pow(xOfDart,2) + Math.pow(yOfDart, 2) <= 1){
            return 10;
        }
        if (Math.pow(xOfDart,2) + Math.pow(yOfDart, 2) <= 25){
            return 5;
        }
        if (Math.pow(xOfDart,2) + Math.pow(yOfDart, 2) <= 100) {
            return 1;
        }
        return 0;

    }
}

