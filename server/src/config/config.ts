import * as dotenvconfig from 'dotenv';

export interface Config {
  mongoDB: string;
}
dotenvconfig.config();

export const settings: Config = {
  mongoDB: process.env.URL || 'google.com',
};
