import { wordList } from '../models/wordList';

export const resolvers = {
  Query: {
    words: () => wordList.find(),
  },
  Mutation: {
    createNewWord: async (_, { name }) => {
      const kitty = new wordList({ name });
      await kitty.save();
      return kitty;
    },
  },
};
