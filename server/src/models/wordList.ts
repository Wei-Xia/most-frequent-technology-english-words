import mongoose from 'mongoose';

export const wordList = mongoose.model('wordList', { name: String });
