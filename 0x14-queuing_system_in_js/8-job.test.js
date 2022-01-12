import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();
const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account',
  },
];

before(() => queue.testMode.enter());
afterEach(() => queue.testMode.clear());
after(() => queue.testMode.exit());

it('display a error message if jobs is not an array', () => {
  expect(() => createPushNotificationsJobs('', queue)).to.throw(
    'Jobs is not an array',
  );
});

it('create two new jobs to the queue', () => {
  createPushNotificationsJobs(jobs, queue);
  expect(queue.testMode.jobs.length).to.equal(2);
  expect(queue.testMode.jobs[0].data).to.equal(jobs[0]);
  expect(queue.testMode.jobs[1].data).to.equal(jobs[1]);
  expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
});
