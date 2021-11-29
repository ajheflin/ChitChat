import IUser from "./user.interface";

export default interface IChat {
  id: string;
  users: [IUser["id"], IUser["id"]] | IUser["id"][]; // a chat can either be with two users ([IUser, IUser]), or with a group (IUser[])
  name: string;
}
