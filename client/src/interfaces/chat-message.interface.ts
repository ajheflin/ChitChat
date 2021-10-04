import IUser from "./user.interface";

export default interface IMessage {
  sender_id: IUser["id"];
  content: File | string;
}
