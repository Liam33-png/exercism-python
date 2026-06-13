import java.util.List;
import java.util.ArrayList;

class HighScores {
    List<Integer> highScores;

    public HighScores(List<Integer> highScores) {
        this.highScores = highScores;
    }

    List<Integer> scores() {
        return this.highScores;
    }

    Integer latest() {
        return this.highScores.get(highScores.size() - 1);
    }

    Integer personalBest() {
        int highest = 0;
        if (this.highScores.size() >= 1){
            highest = this.highScores.get(0);
            for(int number: this.highScores){
                if (number > highest){
                    highest = number;
                }
            }
        }
        return highest;
    }
    
    List<Integer> personalTopThree() {
        List<Integer>copy = new ArrayList<>(this.highScores);
        while (copy.size() > 3){
            int smallest = copy.get(0);
            int smallestPos = 0;
            for (int i = 0; i < copy.size(); i++){
                if (copy.get(i) < smallest){
                    smallest = copy.get(i);
                    smallestPos = i;
                }
            }
            copy.remove(smallestPos);
        }
        copy.sort(null);
        List<Integer>smh = new ArrayList<>();
        for (int i = copy.size() -1 ; i >= 0;i--){
            smh.add(copy.get(i));
        }
        return smh;
        }


}
