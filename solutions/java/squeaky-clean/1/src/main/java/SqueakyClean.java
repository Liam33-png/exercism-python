class SqueakyClean {
    static String clean(String identifier) {
        StringBuilder cleaned = new StringBuilder();
        char[] asArray = identifier.toCharArray();
        boolean apposFound = false;
        for (char character: asArray){
            if (Character.isWhitespace(character)){
                cleaned.append('_');
            }
            else if (character == '-'){
                apposFound = true;
            }
            else if (apposFound){
                    cleaned.append(Character.toUpperCase(character));
                    apposFound = false;
            }
            else if(Character.isDigit(character)){
                switch (character){
                    case '4':
                        cleaned.append('a');
                        break;
                    case '3':
                        cleaned.append('e');
                        break;
                    case '0':
                        cleaned.append('o');
                        break;
                    case '1':
                        cleaned.append('l');
                        break;
                    case '7':
                        cleaned.append('t');
                        break;
                    default:
                        break;
                }
            }
            else if(Character.isLetter(character)) {
                cleaned.append(character);
            }
            }
        return cleaned.toString();
    }
}
