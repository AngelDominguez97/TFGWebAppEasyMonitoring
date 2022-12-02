import { HostModel } from "./host.model"

export interface LastCheckModel{
    
    hostName: string,
    hostIp: string,
    ping: string,
    cpuUsage: number,
    cpuName: string,
    ramUsed: number,
    ramFree: number,
    ramCached: number,
    netIn: number,
    netOut:number
    
}