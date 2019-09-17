import { Cat } from '../models/car';

export const resolvers = {
  Query: {
    hello: () => 'hi',
    cats: () => Cat.find(),
  },
  Mutation: {
    createCat: async (_, { name }) => {
      const kitty = new Cat({ name });
      await kitty.save();
      return kitty;
    },
  },
};
