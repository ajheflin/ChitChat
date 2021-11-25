import IUser from "./user.interface";

export default interface IMessage {
  readonly id: string;
  readonly sender: IUser;
  content: File | string;
}
