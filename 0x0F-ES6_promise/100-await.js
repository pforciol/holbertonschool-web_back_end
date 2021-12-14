import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  return {
    photo: await uploadPhoto(),
    user: await createUser(),
  };
}
