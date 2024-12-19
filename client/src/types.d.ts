export interface trunResponse {
  message: string;
  cell?: [number, number];
  score?: { X: number; O: number };
  winner?: string;
}
