import IUser from "./user.interface";
import IChat from "./chat.interface";

export default interface IMessage {
  created: Date;
  last_modified: Date;
  sender: IUser["id"];
  chat: IChat["id"];
  content: string;
  id: string;
}
