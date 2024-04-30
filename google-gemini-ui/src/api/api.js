import { postAction, getAction, deleteAction, putAction } from "./manage"

export const getAnswer = (id) => getAction("/model-answer/" + id, null)
