class Fighter {

    boolean isVulnerable() {
        return true;
    }

    int getDamagePoints(Fighter fighter) {
        return 1;
    }
}

// TODO: define the Warrior class
class Warrior extends Fighter{
    public String toString(){
        return "Fighter is a Warrior";
    }
    @Override
    public boolean isVulnerable(){
        return false;
    }
    @Override
    public int getDamagePoints(Fighter character){
        return character.isVulnerable() ? 10: 6;
    }
    
    
}

// TODO: define the Wizard class
class Wizard extends Fighter{
    boolean spellPrepared = false;
    
    public String toString(){
        return "Fighter is a Wizard";
    }
    public void prepareSpell(){
        this.spellPrepared = true;
    }
    @Override
    public boolean isVulnerable(){
        return !this.spellPrepared;
    }
    @Override
    public int getDamagePoints(Fighter character){
        return this.spellPrepared ? 12: 3;
    }
}
