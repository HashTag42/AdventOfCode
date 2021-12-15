    class InputAnswerPair {

        public InputAnswerPair(string Input, string Answer) {
            this.Input  = Input;
            this.Answer = Answer;
        }

        public bool IsCorrectAnswer(string Answer) => (this.Answer == Answer);

        public override string ToString() => (Input + " => " + Answer);

        public string Input { get; init; }

        public string Answer { get; init; }
    }