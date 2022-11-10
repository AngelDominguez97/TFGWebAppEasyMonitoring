export class UserModel{
    
    idUser?: number;
    username: string;
    name: string;
    surname: string;
    registerDate: Date;
    updateDate: Date;
    userRole: string;
    constructor(idUser: number, username: string, name: string, surname: string, registerDate: Date, updateDate: Date, userRole: string){
        this.idUser = idUser;
        this.username = username;
        this.name = name;
        this.surname = surname;
        this.registerDate = registerDate;
        this.updateDate = updateDate;
        this.userRole = userRole;
    }
}