public class House {

    public House(Coordinates inPosition) {
        _position.X = inPosition.X;
        _position.Y = inPosition.Y;
        _presents = 1;
    }

    private Coordinates _position = new Coordinates(0,0);
    public Coordinates Position { get => _position; }

    private int _presents { get; set; }
    public int Presents {
        get => _presents;
    }

    public int AddPresent() {
        _presents++;
        return Presents;
    }

    public override string ToString() {
        string output = '[' + Position.ToString() + ":" + Presents + ']';
        return output;
    }
}