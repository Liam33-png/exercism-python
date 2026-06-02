public class LogLevels {
    
    public static String message(String logLine) {
        String [] split = logLine.split(":");
        return split[1].strip();
    }

    public static String logLevel(String logLine) {
        String [] split = logLine.split("]:");
        return split[0].toLowerCase().replace("[", "");
    }

    public static String reformat(String logLine) {
        String [] split = logLine.split(": ");
        return split[1].strip() + " " + split[0].toLowerCase().replace("[", "(").replace("]", ")").strip();
    }
}
