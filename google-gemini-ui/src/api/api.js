import { postAction, getAction, deleteAction, putAction } from "./manage"

export const generateAnswer = (param) => postAction("/generate", param)
