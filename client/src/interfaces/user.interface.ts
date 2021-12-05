import IChat from "./chat.interface";

export default interface IUser {
  name: string;
  username: string;
  email?: string;
  chats: IChat[];
  id: number;
  avatar_url?: string;
}
