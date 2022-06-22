namespace _6kyu_PairOfGloves
{
    using System.Collections.Generic;
    public class Kata
    {
        public static int NumberOfPairs(string[] gloves)
        {
            List<string> oddGloves = new List<string>();
            int pairs = 0;

            foreach (string glove in gloves)
            {
                if (oddGloves.Contains(glove))
                {
                    oddGloves.Remove(glove);
                    pairs++;
                }
                else
                {
                    oddGloves.Add(glove);
                }
            }
            return pairs;
        }
    }
}
