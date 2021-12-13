namespace AoC
{
    class Point
    {
        public int X { get; init; }
        public int Y { get; init; }

        public Point (int X, int Y)
        {
            this.X= X;
            this.Y= Y;
        }

        public override string ToString()
        {
            return (X + "," + Y);
        }
    }
}