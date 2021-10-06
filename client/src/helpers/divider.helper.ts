import IDivider from "@/interfaces/divider.interface";

export const addDividers = <T>(items: T[]) => {
  return items.flatMap((val, i, arr: (T | IDivider)[]) =>
    i !== arr.length - 1 // check for the last item
      ? [val, { divider: true } as IDivider]
      : val
  );
};
