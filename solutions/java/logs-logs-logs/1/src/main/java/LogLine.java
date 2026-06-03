public class LogLine {
    public String logLine;

    public LogLine(String logLine) {
        this.logLine = logLine;
    }

    public LogLevel getLogLevel() {
       String [] logLineBreak = this.logLine.replace("[","").split("]:");
        switch (logLineBreak[0]){
            case "TRC":
                return LogLevel.TRACE;
            case "DBG":
                return LogLevel.DEBUG;
            case "INF":
                return LogLevel.INFO;
            case "WRN":
                return LogLevel.WARNING;
            case"ERR":
                return LogLevel.ERROR;
            case "FTL":
                return LogLevel.FATAL;
            default:
                return LogLevel.UNKNOWN;
        }
    }

    public String getOutputForShortLog() {
        String [] output = this.logLine.split(": ");
        return this.getLogLevel().getEncodedLogLevel() + ":" + output[1];
    }
}
