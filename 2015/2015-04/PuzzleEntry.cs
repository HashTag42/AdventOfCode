class PuzzleEntry {
    public string Input { get; set; }
    public int ExpectedAnswer { get; set; }

    public PuzzleEntry(string inInput, int inAnswer) {
        Input = inInput;
        ExpectedAnswer = inAnswer;
    }

    public bool IsAnswer(int inAnswer) {
        return (ExpectedAnswer == inAnswer);
    }

    public string result(int inAnswer) {
        string message = null;
        message += this.IsAnswer(inAnswer) ? "PASS: " : "FAIL: ";
        message += "Input: " + this.Input;
        message += " // Answer: " + inAnswer;
        message += " // Expected: " + this.ExpectedAnswer;
        return message;
    }
}
