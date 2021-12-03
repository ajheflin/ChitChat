export type ValidationRule = [
  (v: string) => boolean | string,
  (v: string) => boolean | string
];
