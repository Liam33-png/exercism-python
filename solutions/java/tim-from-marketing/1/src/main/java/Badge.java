class Badge {
    public String print(Integer id, String name, String department) {
        String output = "[%d] - %s - %S";
        if (id == null && department == null){
            output = "%s - OWNER";
            return String.format(output,name);
        }
        else if(department == null){
            output = "[%d] - %s - OWNER";
            return String.format(output,id,name);
        }
        else if (id == null){
            output = "%s - %S";
            return String.format(output,name,department);
        }
        else{
            return String.format(output,id,name,department);
        } 
    }
}
