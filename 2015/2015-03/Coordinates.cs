public class Coordinates {
    public Coordinates( int inX, int inY ) {
        X = inX;
        Y = inY;
    }

    public int X { get; set; }
    public int Y { get; set; }

    public override string ToString() {
        return '(' + X.ToString() +  ',' + Y.ToString() + ')';
    }
}