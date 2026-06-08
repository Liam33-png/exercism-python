public class GameMaster {
    public String describe(Character character){
        return String.format("You're a level %d %s with %d hit points.", character.getLevel(), character.getCharacterClass(), character.getHitPoints());
    }
    public String describe(TravelMethod travelMethod){
        String word = travelMethod == TravelMethod.HORSEBACK  ? "on" : "by";
        String destination = travelMethod == TravelMethod.HORSEBACK ? "horseback" : "walking";
        return String.format("You're traveling to your destination %s %s.", word,destination);
    }
    public String describe(Destination destination){
        return String.format("You've arrived at %s, which has %d inhabitants.", destination.getName(), destination.getInhabitants());
    }
    // TODO: define a 'describe' method that returns a description of a Character, Destination and TravelMethod
    public String describe(Character character, Destination destination, TravelMethod travelMethod){
        return describe(character) + " " + describe(travelMethod) + " " + describe(destination);
    }
    public String describe(Character character, Destination destination){
        return describe(character) + " " + describe(TravelMethod.WALKING) + " " + describe(destination);
    }
}
