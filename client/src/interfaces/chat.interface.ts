import IMessage from "./chat-message.interface";
import IUser from "./user.interface";

export default interface IChat {
  id: string;
  users: [IUser, IUser] | IUser[]; // a chat can either be with two users ([IUser, IUser]), or with a group (IUser[])
  messages: IMessage[]; // messages for a given chat
}
