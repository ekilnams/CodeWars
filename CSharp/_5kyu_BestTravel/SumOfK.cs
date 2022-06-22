namespace _5kyu_BestTravel
{
    using System;
    using System.Collections.Generic;
    using System.Linq;

    public static class SumOfK
    {
        public static int? chooseBestSum(int t, int k, List<int> ls)
        {
            Console.WriteLine($"t:{t} k:{k} ls:{ls}");

            if (k > ls.Count)
                return null;

            if (k == ls.Count)
            {
                int sum = ls.Sum();
                if (sum > t)
                    return null;
                else
                    return sum;
            }

            ls.Sort();

            return bestSumRecursive(t, k, ls);
        }

        public static int? bestSumRecursive(int t, int k, List<int> ls)
        {
            if (k == 0)
                return 0;

            int? bestSum = null;
            for (int i = 0; i < ls.Count; i++)
            {
                int testValue = ls[i];
                int remaining = t - testValue;
                List<int> remainingValues = new List<int>(ls);
                remainingValues.RemoveAt(i);

                int? newSum = testValue + bestSumRecursive(remaining, k - 1, remainingValues);

                if (newSum > t)
                    break;

                bestSum = Nullable.Compare(bestSum, newSum) > 0 ? bestSum : newSum;
            }

            return bestSum;
        }
    }
}
