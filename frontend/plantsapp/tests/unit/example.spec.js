import { expect } from 'chai'
import { mount } from '@vue/test-utils'
import Tests from '@/views/Tests.vue'

describe('Tests.vue', () => {
  it('renders props.msg when passed', () => {
    const wrapper = mount(Tests)
    expect(wrapper.exists()).toBe(true)
  })
})
