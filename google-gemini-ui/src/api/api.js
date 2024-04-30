import { postAction, getAction, deleteAction, putAction } from "./manage"

export const generateAnswer = (param) => postAction("/generate-answer", param)

export const gameSetup = (param) => postAction("/game-setup", param)
