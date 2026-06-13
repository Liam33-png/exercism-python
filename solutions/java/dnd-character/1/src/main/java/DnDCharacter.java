import java.util.List;
import java.util.Random;
import java.util.ArrayList;

class DnDCharacter {
    int strength = ability(rollDice());
    int dexterity = ability(rollDice());
    int constitution = ability(rollDice());
    int intelligence = ability(rollDice());
    int wisdom = ability(rollDice());
    int charisma = ability(rollDice());
    int hitpoints = 10 + modifier(constitution);

    int ability(List<Integer> scores) {
        List<Integer> sorted = new ArrayList<>(scores);
        for (int i = 0; i < sorted.size(); i++){
            int lowest = sorted.get(i);
            int lowestPosition = i;
            for (int j = i; j < sorted.size(); j++){
                if (sorted.get(j) < lowest){
                    lowest = sorted.get(j);
                    lowestPosition = j;
                }
            }
            int temp = sorted.get(i);
            sorted.set(i,lowest);
            sorted.set(lowestPosition,temp);
        }
        int total = 0;
        for (int i = 1; i < sorted.size(); i++){
            total += sorted.get(i);
        }
        return total;
    }
    List<Integer> rollDice() {
        List<Integer> diceRolls = new ArrayList<>();
        Random random = new Random();
        while (diceRolls.size() < 4){
            diceRolls.add(random.nextInt(6) + 1);
        }
        return diceRolls;
    }

    int modifier(int input) {
        return Math.floorDiv(input - 10, 2);
    }

    int getStrength() {
        return this.strength;
    }

    int getDexterity() {
        return this.dexterity;
    }

    int getConstitution() {
        return this.constitution;
    }

    int getIntelligence() {
        return this.intelligence;
    }

    int getWisdom() {
        return this.wisdom;
    }

    int getCharisma() {
        return this.charisma;
        
    }

    int getHitpoints() {
        return this.hitpoints;
    }
}
