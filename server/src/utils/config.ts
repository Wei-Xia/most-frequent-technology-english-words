import * as dotenvconfig from 'dotenv';

export interface Config {
  mongodbURL: string;
}
dotenvconfig.config();

export const settings: Config = {
  mongodbURL: process.env.mongodbURL || '',
};
