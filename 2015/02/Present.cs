using System;

public class Present: Package
{
    public uint PaperArea { get; }
    public uint RibbonLength { get; }

    public Present(string textDimensions): base(textDimensions)
    {
        uint surfaceArea = (2*Length*Width) + (2*Width*Height) + (2*Height*Length);
        uint slackArea = Dimensions[0] * Dimensions[1];
        PaperArea = surfaceArea + slackArea;

        uint ribbon = Dimensions[0]*2 + Dimensions[1]*2;
        uint bow = Dimensions[0]*Dimensions[1]*Dimensions[2];
        RibbonLength = ribbon + bow;
    }
}