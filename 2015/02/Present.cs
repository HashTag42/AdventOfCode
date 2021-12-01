using System;

public class Present
{
    public uint Length { get; }
    public uint Width { get; }
    public  uint Height { get; }
    public uint PaperArea { get; }
    public uint RibbonLength { get; }
    private uint[] Dimensions { get; }

    public Present(string textDimensions)
    {
        string[] terms = textDimensions.Split('x');

        Dimensions = new uint[3];
        Length  = Dimensions[0] = uint.Parse(terms[0]);
        Width   = Dimensions[1] = uint.Parse(terms[1]);
        Height  = Dimensions[2] = uint.Parse(terms[2]);

        Array.Sort(Dimensions);

        uint surfaceArea = (2*Length*Width) + (2*Width*Height) + (2*Height*Length);
        uint slackArea = Dimensions[0] * Dimensions[1];
        PaperArea = surfaceArea + slackArea;

        uint ribbon = Dimensions[0]*2 + Dimensions[1]*2;
        uint bow = Dimensions[0]*Dimensions[1]*Dimensions[2];
        RibbonLength = ribbon + bow;
    }
}