class Lanternfish {
    private int _days { get; set; }

    public int Days { get => _days; }

    public Lanternfish() {
        _days = 8;
    }

    public Lanternfish(int inDays) {
        _days = inDays;
    }

    public bool NextDay() {
        bool newFish = false;
        if( _days == 0) {
            _days = 6;
            newFish = true;
        } else {
            _days--;
        }
        return newFish;
    }
}